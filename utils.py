import os
import re

# group 1 - bouquet name
# group 2 - bouquet size
# group 3 - flowers [(flower quantity, flower specie), ...]
# group 5 - total quantity of flowers in the bouquet
from dataclasses import dataclass
from itertools import groupby
from typing import List, Tuple

bouquet_design_pattern = re.compile(r"^([A-Z])([S,L])((\d+[a-z])+)(\d+)$")
bouquet_pattern = re.compile(r"^([A-Z])([S,L])((\d+[a-z])+)$")
flower_pattern = re.compile(r"\d+[a-z]")


def is_valid_bouquet_design(bouquet_design: str) -> bool:
    """
    Validate bouquet design.
    <bouquet name><bouquet size><flower 1 quantity><flower 1
    specie>...<flower N quantity><flower N specie><total quantity of
    flowers in the bouquet>
    """
    if bouquet_design_pattern.match(bouquet_design):
        return True
    else:
        return False


@dataclass
class BouquetFlower:
    quantity: int
    specie: str


@dataclass
class BouquetDesign:
    name: str
    size: str
    flowers: List[BouquetFlower]
    total_quantity: int


@dataclass
class Bouquet:
    name: str
    size: str
    flowers: List[BouquetFlower]


def parse_bouquet_design(bouquet_design: str) -> BouquetDesign:
    """
    Pare bouquet design raw data
    """
    bouquet_design_data = bouquet_design_pattern.match(bouquet_design)

    bouquet_design = BouquetDesign(
        name=bouquet_design_data.group(1),
        size=bouquet_design_data.group(2),
        flowers=[
            BouquetFlower(
                quantity=int(f[:-1]),
                specie=f[-1]
            ) for f in flower_pattern.findall(bouquet_design_data.group(3))
        ],
        total_quantity=int(bouquet_design_data.group(5)),
    )

    return bouquet_design


def parse_bouquet(bouquet: str) -> Bouquet:
    """
    Pare bouquet raw data
    """
    bouquet_data = bouquet_pattern.match(bouquet)

    bouquet = Bouquet(
        name=bouquet_data.group(1),
        size=bouquet_data.group(2),
        flowers=[
            BouquetFlower(
                quantity=int(f[:-1]),
                specie=f[-1]
            ) for f in flower_pattern.findall(bouquet_data.group(3))
        ],
    )

    return bouquet


def parse_sample_file(file_path):
    """
    Pare sample file
    """

    with open(file_path) as f:
        bouquet_design_templates, all_flowers = \
            [list(group) for k, group in groupby(f.readlines(), lambda x: x == "\n") if not k]

    all_flowers = [f.rstrip('\n') for f in all_flowers if f]
    bouquet_design_templates = [b.rstrip('\n') for b in bouquet_design_templates if b]

    return bouquet_design_templates, all_flowers
