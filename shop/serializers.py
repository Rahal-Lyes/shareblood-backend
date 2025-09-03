from rest_framework import serializers
from .models import Product,Category


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Category
    fields="__all__"   

class ProductSerializer(serializers.ModelSerializer):
   # On affiche la catégorie en détail + possibilité d’ajouter un champ read-only
    category = CategorySerializer(read_only=True)
    # On ajoute un champ pour créer/mettre à jour via l’ID de la catégorie
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    class Meta:
      model=Product
      fields=['id','product_name','description','price','stock','is_available','image','category','category_id',]    