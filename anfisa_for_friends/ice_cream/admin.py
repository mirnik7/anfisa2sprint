from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
# admin.site.empty_value_display = 'Не задано' 


# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # Какие поля будут показаны на странице списка объектов, это кортеж
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )

    # Какие поля можно редактировать прямо на странице списка объектов, это кортеж
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )

    # Кортеж с перечнем полей, по которым будет проводиться поиск. 
    # Форма поиска отображается над списком элементов.
    search_fields = ('title',)

    # Кортеж с полями, по которым можно фильтровать записи. 
    # Фильтры отобразятся справа от списка элементов.
    list_filter = ('category', )

    # В этом кортеже указываются поля, при клике на которые можно перейти
    # на страницу просмотра и редактирования записи. 
    # По умолчанию такой ссылкой служит первое отображаемое поле.
    list_display_links = ('title',)

    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    empty_value_display = 'Не задано'

    # Чтобы связанные записи можно было перекладывать из одного окошка в другое
    # указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# На страницу редактирования категории можно подгрузить блок с информацией о связанных с ней сортах мороженого
# Подготавливаем модель IceCream для вставки на страницу другой модели. (2-й вариант - admin.TabularInline)
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )


# Регистрируем новый класс:
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin
admin.site.register(IceCream, IceCreamAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
