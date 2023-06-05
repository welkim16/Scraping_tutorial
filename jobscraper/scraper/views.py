from django.shortcuts import render
from .models import JbDate
from rest_framework import viewsets
from .serializers import JobSerializer
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

link = 'https://www.brightermonday.co.ke/jobs'
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
divs = soup.find_all('div',class_="mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500")

for para in divs:
    savs=JbDate()
    job_title = para.find('div',class_="flex items-center").find('p',class_='text-lg font-medium break-words text-link-500').get_text().strip()
    dates = para.find('div',class_="flex flex-row items-start items-center px-5 py-3 w-full border-t border-gray-300").find('p', class_='ml-auto text-sm font-normal text-gray-700 text-loading-animate').get_text().strip()
    if dates is not None:
        savs.scraped_date=dates
    savs.job_title=job_title
    savs.save()
class JobViewSet(viewsets.ModelViewSet):
    queryset = JbDate.objects.all()
    serializer_class = JobSerializer
