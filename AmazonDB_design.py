from sqlalchemy import create_engine, 
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    category = Column(String)
    stock = Column(Integer)
    image = Column(String)
    rating = Column(Float)
    review = Column(String)
    size = Column(String)
    color = Column(String)
    brand = Column(String)
    is_prime = Column(Boolean)

class product_review(Base):
    __tablename__ = 'product_reviews'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Float)
    review = Column(String)
    review_date = Column(DateTime)
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    country = Column(String)
    phone = Column(String)
    alt_phone = Column(String)
    is_prime = Column(Boolean)
    
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    total = Column(Float)
    order_date = Column(DateTime)
    delivery_date = Column(DateTime)
    status = Column(String)
    payment_method = Column(String)
    payment_status = Column(String)
    shipping_address = Column(String)
    shipping_city = Column(String)
    shipping_state = Column(String)
    shipping_zip = Column(String)
    shipping_country = Column(String)
    shipping_phone = Column(String)
    shipping_alt_phone = Column(String)
    shipping_is_prime = Column(Boolean)

class order_details(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    total = Column(Float)
    
class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    total = Column(Float)
    cart_date = Column(DateTime)
    
class Wishlist(Base):
    __tablename__ = 'wishlists'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    wishlist_date = Column(DateTime)
    