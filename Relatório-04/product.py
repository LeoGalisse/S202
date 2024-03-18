from database.database import Database

class ProductAnalyzer:
    def __init__(self, database: Database):
        _database = database
        db = _database
        self.collection = db.collection

    def total_sales_per_day(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ]
        return list(self.collection.aggregate(pipeline))

    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ]
        return list(self.collection.aggregate(pipeline))

    def top_spending_customer(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        return list(self.collection.aggregate(pipeline))

    def products_sold_above_quantity(self, quantity):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": quantity}}},
            {"$group": {"_id": "$produtos.nome", "total_vendido": {"$sum": "$produtos.quantidade"}}}
        ]
        return list(self.collection.aggregate(pipeline))
