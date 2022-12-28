from django.shortcuts import render

import requests
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Divvy_Bikes(APIView):
    def post(self,request):
        try:
            response = requests.get("https://gbfs.divvybikes.com/gbfs/en/station_status.json")
            data = response.json()
            total_docks_avl = 0
            total_bikes_avl = 0
            total_station_active = 0
            total_bikes_reserved = 0

            for i in data["data"]["stations"]:
                total_docks_avl += i["num_docks_available"]
                total_bikes_avl += i["num_bikes_available"]
                if i["station_status"]=="active":
                    total_station_active += 1

            response1 = requests.get("https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json")
            data1 = response1.json()
            for i in data1["data"]["bikes"]:
                total_bikes_reserved += i["is_reserved"]


            return Response({
                "Total Docks Avl":total_docks_avl,
                "Total Bikes Avl":total_bikes_avl,
                "Total Station Active":total_station_active,
                "Total Bikes Reserved":total_bikes_reserved
            },status=status.HTTP_200_OK)
        except:
            return Response({"message":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

