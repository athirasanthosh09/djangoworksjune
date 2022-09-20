from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer

#
# class ProductsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside product get"})
#
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"Good Morning"})
#
#
# class EveningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"good evening"})
#
#
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)+int(n2)
#         return Response({"msg":res})
#
class SubView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=int(n1)-int(n2)
        return Response({"msg":res})
#

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({"msg":res})

class NumcheckView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=""
        if n%2==0:
            res="number is even"
        else:
            res="number is odd"

        #return Response({"result":res})
        return Response(data=res)

class FactView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=1
        for i in range(1,n+1):
            res=res*i
        return Response(data=res)

class WordcountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("text")
        word=txt.split(" ")
        wordcount={}
        for w in word:
            if w in wordcount:
                wordcount[w]+=1
            else:

                wordcount[w]=1


        return Response(data=wordcount)


    #armstrong,pallindrome,prime

class PrimeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=""
        f=0
        for i in range(1,n+1):
            if n%i==0:
                f=f+1
            if f==2:
                res="Number is prime "
            else:
                res="Number is not a prime"
        return Response(data=res)

class PallindromeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=""
        rev=0
        m=n
        while n>0:
            rm=n%10
            rev=rev*10+rm
            n=n//10
        if m==rev:
            res="The Number is Pallindrome"
        else:
            res="The Number is not a Pallindrome"
        return Response(data=res)

class ArmstronView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        result=""
        res=0
        b=n
        while n>0:
            c=n%10
            res=res+c*c*c
            n=n//10
        if b==res:
            result="It is an Armstrong Number"
        else:
            result="Not an Armstrong Number"
        return Response(data=result)


class ProductView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)

        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        # bname=request.data.get("name")
        # bauthor=request.data.get("author")
        # bprice=request.data.get("price")
        # bpublisher=request.data.get("publisher")
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
        # return Response(data="created")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)

    def delete(self,req,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

    def put(self,req,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=req.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ReviewsView(APIView):

    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ReviewDetailView(APIView):


    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,req,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=qs,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return  Response(data=serializer.errors)

    def delete(self,req,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")





