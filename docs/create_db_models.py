# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Category(Base):
    """description: Represents a product category."""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Supplier(Base):
    """description: Represents suppliers of food products."""
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)

class Product(Base):
    """description: Represents food products available for sale."""
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

class Customer(Base):
    """description: Represents customers who purchase products."""
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(Text, nullable=True)

class Order(Base):
    """description: Represents orders placed by customers."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float, default=0.0)

class OrderDetail(Base):
    """description: Represents detailed line items within an order."""
    __tablename__ = 'order_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    line_total = Column(Float, nullable=False)

class Review(Base):
    """description: Represents customer reviews for products."""
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)

class Discount(Base):
    """description: Represents discounts applicable to products."""
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    description = Column(String, nullable=True)
    discount_percent = Column(Float, nullable=False)

class Payment(Base):
    """description: Represents payments made by customers for orders."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)

class Shipment(Base):
    """description: Represents shipment details for orders."""
    __tablename__ = 'shipment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    shipment_date = Column(DateTime, nullable=True)
    delivery_date = Column(DateTime, nullable=True)
    shipment_status = Column(String, nullable=False)

class Promotion(Base):
    """description: Represents promotional campaigns for marketing."""
    __tablename__ = 'promotion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    description = Column(Text, nullable=True)

class Cart(Base):
    """description: Represents shopping cart items for customers."""
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)

class News(Base):
    """description: Represents news articles/ads to inform customers about updates and promotions."""
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    publication_date = Column(DateTime, default=datetime.datetime.utcnow)

# Create SQLite database and tables
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample Data Insertion

categories = [
    Category(name="Rice"),
    Category(name="Snacks"),
    Category(name="Spices"),
    Category(name="Sauces"),
]

suppliers = [
    Supplier(name="Asia Foods Inc.", contact_info="asiafoods@example.com"),
    Supplier(name="Oriental Delights", contact_info="orientaldelights@example.com"),
    Supplier(name="Spice Traders", contact_info="spicetraders@example.com"),
]

products = [
    Product(name="Basmati Rice", description="Premium quality Basmati rice", category_id=1, supplier_id=1, price=10.0, stock_quantity=50),
    Product(name="Nori Seaweed", description="Seaweed for sushi", category_id=2, supplier_id=2, price=5.0, stock_quantity=100),
    Product(name="Sriracha Sauce", description="Spicy Sriracha sauce", category_id=4, supplier_id=1, price=3.5, stock_quantity=80),
]

customers = [
    Customer(name="John Doe", email="john.doe@example.com", phone="1234567890", address="123 Elm Street"),
    Customer(name="Jane Smith", email="jane.smith@example.com", phone="0987654321", address="456 Maple Avenue"),
]

orders = [
    Order(customer_id=1, order_date=datetime.datetime.now(), total_amount=40.5),
    Order(customer_id=2, order_date=datetime.datetime.now(), total_amount=7.0),
]

order_details = [
    OrderDetail(order_id=1, product_id=1, quantity=2, unit_price=10.0, line_total=20.0),
    OrderDetail(order_id=1, product_id=3, quantity=5, unit_price=3.5, line_total=17.5),
    OrderDetail(order_id=2, product_id=2, quantity=1, unit_price=5.0, line_total=5.0),
]

reviews = [
    Review(customer_id=1, product_id=1, rating=5, comment="Great quality rice."),
    Review(customer_id=2, product_id=3, rating=4, comment="Spicy and flavorful."),
]

discounts = [
    Discount(product_id=1, description="10% off on premium rice", discount_percent=10.0),
]

payments = [
    Payment(order_id=1, payment_date=datetime.datetime.now(), amount=40.5, payment_method="Credit Card"),
    Payment(order_id=2, payment_date=datetime.datetime.now(), amount=7.0, payment_method="PayPal"),
]

shipments = [
    Shipment(order_id=1, shipment_date=datetime.datetime.now(), delivery_date=datetime.datetime.now() + datetime.timedelta(days=2), shipment_status="Delivered"),
    Shipment(order_id=2, shipment_date=datetime.datetime.now(), delivery_date=None, shipment_status="Pending"),
]

promotions = [
    Promotion(name="Summer Sale", start_date=datetime.datetime.now(), end_date=datetime.datetime.now() + datetime.timedelta(days=30), description="Discounts on selected items during summer."),
]

carts = [
    Cart(customer_id=1, product_id=3, quantity=2),
    Cart(customer_id=2, product_id=1, quantity=1),
]

news_items = [
    News(title="Grand Opening Sale!", content="Join us for our grand opening with huge discounts across all products.", publication_date=datetime.datetime.now() - datetime.timedelta(days=10)),
    News(title="New Product Launch", content="We are excited to introduce our new line of organic spices.", publication_date=datetime.datetime.now()),
]

# Adding sample data to session
session.add_all(categories + suppliers + products + customers + orders + order_details + reviews +
                discounts + payments + shipments + promotions + carts + news_items)
session.commit()
