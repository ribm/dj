from rest_framework import serializers
from .models import Employee


class EmployeESerializers(serializers.ModelSerializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=100)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=100)
    class Meta:
        model=Employee
        fields= "__all__"

    def validate_esal(self,value):
        if value>100:
            raise  serializers.ValidationError("must be more than 100")
        return value


    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename = validated_data.get('ename',instance.ename)
        instance.esal = validated_data.get('eno',instance.esal)
        instance.eaddr = validated_data.get('eno',instance.eaddr)
        instance.save()
        return instance

