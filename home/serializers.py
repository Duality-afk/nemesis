from rest_framework import serializers
from home.models import Account
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 250)
    username = serializers.CharField(max_length = 250)
    password = serializers.CharField(max_length = 150)


    class Meta:
        model = Account
        fields = ('email','username','password','address')


    def validate(self, args):
        email = args.get('email',None)
        username = args.get('username',None)
        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exists')})
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exists')})

        return super().validate(args)

    def create(self,validated_data):
        return Account.objects.create_user(**validated_data)
