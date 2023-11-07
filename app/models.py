from sqlalchemy import Column, Integer, String,Float ,ForeignKey
from app import db
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__='category'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),nullable=False,unique=True)
    products = relationship("Product",backref = 'category', lazy = True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer,ForeignKey(Category.id), nullable=False)


if __name__=="__main__":
    from app import app
    with app.app_context():
        c1 = Category(name="mobile")
        c2 = Category(name="Tablet")
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        p1 = Product(name="Galaxy", price=2400, category_id=1,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg')
        p2 = Product(name="iphone", price=2300, category_id=2,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg')
        p3 = Product(name="tab s9", price=2000, category_id=1,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg')
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.commit()
        #db.create_all()

