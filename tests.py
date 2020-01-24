import os

import pytest

from generate_bouquet import FlowerStore
from utils import parse_bouquet, Bouquet, BouquetDesign, parse_bouquet_design, parse_sample_file


@pytest.yield_fixture
def test_file() -> str:
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(__location__, "flowers.txt")


def test_flower_store(test_file):
    # prepare data
    bouquet_design_templates, all_flowers = parse_sample_file(test_file)

    flower_store = FlowerStore(all_flowers=all_flowers, infinity_flower_store=False)

    for bouquet_design_template in bouquet_design_templates:
        generated_bouquet = flower_store.get_bouquet(bouquet_design_template)

        assert bouquet_design_template[:-2] in generated_bouquet

        bouquet: Bouquet = parse_bouquet(generated_bouquet)
        bouquet_design: BouquetDesign = parse_bouquet_design(bouquet_design_template)

        assert bouquet.size == bouquet_design.size
        assert bouquet.name == bouquet_design.name
        assert sum([f.quantity for f in bouquet.flowers]) == bouquet_design.total_quantity
