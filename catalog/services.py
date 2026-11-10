from catalog.models import Product


class ProductService:

    @staticmethod
    def get_products_by_category(category_id):
        return list(Product.objects.filter(product_category_id=category_id))