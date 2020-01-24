"""
Flower Store

bouquet design template
<bouquet name><bouquet size><flower 1 quantity><flower 1
specie>...<flower N quantity><flower N specie><total quantity of
flowers in the bouquet>

bouquet template
<bouquet name><bouquet size><flower 1 quantity><flower 1
specie>...<flower N quantity><flower N specie>
"""
import random
import sys
from collections import defaultdict
from typing import List, Optional

from utils import is_valid_bouquet_design, parse_bouquet_design, BouquetDesign, BouquetFlower, parse_sample_file


class FlowerStore:
    """Small flower store"""

    def __init__(self, all_flowers: List[str], infinity_flower_store: bool = False):

        # flowers in store, small and large flowers
        self.flowers_store = {
            "L": defaultdict(int),
            "S": defaultdict(int)
        }
        self.total_flowers_quantity_in_store = defaultdict(int)

        # init flower store
        for flower in all_flowers:
            size = flower[-1]
            species = flower[0]
            self.flowers_store[size][species] += 1
            # store quantity of S (small) and L (large) flowers in store
            self.total_flowers_quantity_in_store[flower[-1]] += 1

        # if True - don't delete flowers that were used for generate bouquets
        self.infinity_flower_store = infinity_flower_store

    def get_bouquet(self, bouquet_design_template: str) -> str:
        """Get bouquet"""

        # validate bouquet_design_template
        if not is_valid_bouquet_design(bouquet_design_template):
            raise ValueError(f"{bouquet_design_template} - bouquet design template is not valid")

        # parse bouquet_design
        bouquet_design: BouquetDesign = parse_bouquet_design(bouquet_design_template)

        # validate total_quantity
        if bouquet_design.total_quantity < sum([f.quantity for f in bouquet_design.flowers]):
            raise ValueError(f"{bouquet_design_template} - "
                             f"total_quantity can't be less the sum of all flowers quantity")

        if self.can_generate_bouquet(bouquet_design):
            # take flowers from store
            if not self.infinity_flower_store:
                self._take_flowers(bouquet_design)

            return self._generate_bouquet(bouquet_design)
        else:
            return "Can't generate a bouquet"

    def _take_flowers(self, bouquet_design: BouquetDesign, flowers: Optional[List[BouquetFlower]] = None):
        """Take (remove) needed flowers for a bouquet from store"""

        if flowers is None:
            flowers = bouquet_design.flowers
        for flower in flowers:
            self.flowers_store[bouquet_design.size][flower.specie] -= flower.quantity

    def can_generate_bouquet(self, bouquet_design: BouquetDesign):
        """Check that e have enough flowers in the store"""

        # do we have needed flowers
        for flower in bouquet_design.flowers:
            if (not self.flowers_store[bouquet_design.size].get(flower.specie) or
                    self.flowers_store[bouquet_design.size][flower.specie] < flower.quantity):
                return False
        # can we fill extra space in the bouquet with any kind of flowers
        # (for small bouquets only small flowers, for large bouquets - large flowers)
        if self.total_flowers_quantity_in_store[bouquet_design.size] < bouquet_design.total_quantity:
            return False
        return True

    def _generate_bouquet(self, bouquet_design: BouquetDesign) -> str:
        """Generate a bouquet"""

        # generate a base bouquet
        bouquet = f"{bouquet_design.name}" \
                  f"{bouquet_design.size}" \
                  f"{''.join([f'{f.quantity}{f.specie}' for f in bouquet_design.flowers])}"
        # need to fill extra space in the bouquet with any kind of flowers
        extra_flowers_quantity = \
            bouquet_design.total_quantity - sum([f.quantity for f in bouquet_design.flowers])

        extra_flowers = self._extra_flowers(extra_flowers_quantity, bouquet_design)

        return bouquet + extra_flowers

    def _extra_flowers(self, extra_flowers_quantity: int, bouquet_design: BouquetDesign) -> str:
        """Get extra flowers"""

        if extra_flowers_quantity:
            specie, quantity = random.choice(list(self.flowers_store[bouquet_design.size].items()))
            quantity_to_take = quantity if quantity <= extra_flowers_quantity else extra_flowers_quantity
            if not self.infinity_flower_store:
                self._take_flowers(bouquet_design, [BouquetFlower(specie=specie, quantity=quantity_to_take)])
            return f"{quantity_to_take}{specie}" + self._extra_flowers(
                extra_flowers_quantity-quantity_to_take, bouquet_design
            )
        return ""


if __name__ == "__main__":
    print("⚘.⚘.⚘______Flower store_____⚘.⚘.⚘")
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = input("Provide a path to yours <sample.txt> file with data: ")
    bouquet_design_templates, all_flowers = parse_sample_file(file_path)

    flower_store = FlowerStore(all_flowers)
    for bouquet_design_template in bouquet_design_templates:
        bouquet = flower_store.get_bouquet(bouquet_design_template)
        print(f"For the bouquet design: {bouquet_design_template} - was generated a bouquet: {bouquet}")
