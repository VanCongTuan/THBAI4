from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product

admin = Admin(app, name="Quan ly ban hang", template_mode="bootstrap4")


class MyproductView(ModelView):
    column_display_pk = True
    column_list = ['name', 'price']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    can_export = True


class MyCategoryView(ModelView):
    column_display_pk = True
    column_list = ['name']
    column_searchable_list = ['name']
    column_filters = ['name']


class MyStarts(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/status.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyproductView(Product, db.session))
admin.add_view(MyStarts(name="Báo Cáo Thông Kê"))
