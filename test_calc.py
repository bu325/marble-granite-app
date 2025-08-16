import unittest
from core.services.calc import (
    area_m2, purchase_cost, sell_price, pre_discount_total,
    discount, taxable_base, tax_amount, final_total,
    profit_margin, net_profit
)

class TestCalc(unittest.TestCase):

    def test_area_m2(self):
        self.assertAlmostEqual(area_m2(2, 3, 1), 6.0)
        self.assertAlmostEqual(area_m2(1.5, 2, 2), 6.0)
        self.assertAlmostEqual(area_m2(0, 0, 0), 0.0)
        with self.assertRaises(ValueError):
            area_m2(-1, 2, 1)

    def test_purchase_cost(self):
        # Mock InvoiceItem objects
        class MockInvoiceItem:
            def __init__(self, area_m2, buy_price_m2):
                self.area_m2 = area_m2
                self.buy_price_m2 = buy_price_m2

        items = [
            MockInvoiceItem(10, 50),
            MockInvoiceItem(5, 100)
        ]
        self.assertAlmostEqual(purchase_cost(items), 10 * 50 + 5 * 100)
        self.assertAlmostEqual(purchase_cost([]), 0.0)
        with self.assertRaises(ValueError):
            purchase_cost([MockInvoiceItem(-1, 10)])

    def test_sell_price(self):
        class MockInvoiceItem:
            def __init__(self, area_m2, sell_price_m2):
                self.area_m2 = area_m2
                self.sell_price_m2 = sell_price_m2

        items = [
            MockInvoiceItem(10, 70),
            MockInvoiceItem(5, 120)
        ]
        self.assertAlmostEqual(sell_price(items), 10 * 70 + 5 * 120)
        self.assertAlmostEqual(sell_price([]), 0.0)
        with self.assertRaises(ValueError):
            sell_price([MockInvoiceItem(10, -1)])

    def test_pre_discount_total(self):
        self.assertAlmostEqual(pre_discount_total(100, 10, 20), 130.0)
        self.assertAlmostEqual(pre_discount_total(0, 0, 0), 0.0)
        with self.assertRaises(ValueError):
            pre_discount_total(-10, 10, 20)

    def test_discount(self):
        self.assertAlmostEqual(discount(100, 10), 10.0)
        self.assertAlmostEqual(discount(200, 0), 0.0)
        self.assertAlmostEqual(discount(0, 10), 0.0)
        with self.assertRaises(ValueError):
            discount(-100, 10)

    def test_taxable_base(self):
        self.assertAlmostEqual(taxable_base(100, 10), 90.0)
        self.assertAlmostEqual(taxable_base(100, 0), 100.0)
        self.assertAlmostEqual(taxable_base(10, 10), 0.0)
        with self.assertRaises(ValueError):
            taxable_base(-100, 10)
        with self.assertRaises(ValueError):
            taxable_base(10, 20) # Should raise error if base becomes negative

    def test_tax_amount(self):
        self.assertAlmostEqual(tax_amount(100, 10), 10.0)
        self.assertAlmostEqual(tax_amount(100, 0), 0.0)
        self.assertAlmostEqual(tax_amount(0, 10), 0.0)
        with self.assertRaises(ValueError):
            tax_amount(-100, 10)

    def test_final_total(self):
        self.assertAlmostEqual(final_total(90, 10), 100.0)
        self.assertAlmostEqual(final_total(0, 0), 0.0)
        with self.assertRaises(ValueError):
            final_total(-90, 10)

    def test_profit_margin(self):
        self.assertAlmostEqual(profit_margin(700, 10, 20, 500, 5), 225.0)
        self.assertAlmostEqual(profit_margin(0, 0, 0, 0, 0), 0.0)
        with self.assertRaises(ValueError):
            profit_margin(-700, 10, 20, 500, 5)

    def test_net_profit(self):
        self.assertAlmostEqual(net_profit(225, 50, 25), 150.0)
        self.assertAlmostEqual(net_profit(0, 0, 0), 0.0)
        with self.assertRaises(ValueError):
            net_profit(-225, 50, 25)

if __name__ == '__main__':
    unittest.main()


