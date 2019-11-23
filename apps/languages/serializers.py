from rest_framework import serializers
from .models import language, Paradigm, Programmer

'''
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = language
        fields = '__all__'

#MOSTRAR LINKS
class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['id', 'name', 'url']

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    paradigm = ParadigmSerializer(many=False, read_only=True)    
    class Meta:
        model = language
        fields = ['id', 'name', 'paradigm', 'url']


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True) #OCULTA EL HIPERVINCULO Y SOLO APARECE LA RELACION
    
    class Meta:
        model = Programmer
        fields = ['id', 'name', 'languages', 'url']
'''
#ESCONDER LAS URL Y VER EN POSTMAN


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['id', 'name']

class LanguageSerializer(serializers.ModelSerializer):
    paradigm = ParadigmSerializer(many=False, read_only=True)    
    class Meta:
        model = language
        fields = ['id', 'name', 'paradigm']


class ProgrammerSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True) #OCULTA EL HIPERVINCULO Y SOLO APARECE LA RELACION
    
    class Meta:
        model = Programmer
        fields = ['id', 'name', 'languages']
