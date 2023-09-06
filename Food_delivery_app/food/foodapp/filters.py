from ast import Expression
from cgitb import lookup
from dataclasses import field
from random import choices
import django_filters
from django_filters import CharFilter, RangeFilter
from .models import *

class FoodFilter(django_filters.FilterSet):
    CHOICES =(
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    
    price = RangeFilter()
    ordering = django_filters.ChoiceFilter(label='Order by price', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = FoodModel
        fields = {
            'name' : ['icontains'],
            'allergens' : ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)


class LogFilter(django_filters.FilterSet):
    CHOICES =(
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    
    ordering = django_filters.ChoiceFilter(label='Order by level', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Logger
        fields = {
            'user' : ['icontains'],
            'ipaddress' : ['icontains'],
            'requestMethod' : ['icontains'],
            'viewFunctionCalled' : ['icontains'],
            'priorityString' : ['icontains'],
        }


    def filter_by_order(self, queryset, name, value):
        expression = 'priorityInt' if value == 'ascending' else '-priorityInt'
        return queryset.order_by(expression)