from django.shortcuts import render
from rest_framework.views import APIView, Response
from datetime import datetime
from django.http import JsonResponse


def get_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


class GetAge(APIView):

    def post(self, request):
        day = request.data['day']
        month = request.data['month']
        year = request.data['year']
        date_of_birth = datetime(year=int(year), month=int(month), day=int(day))
        current_date = datetime.today()
        current_year = datetime.today().year
        current_month = datetime.today().year
        current_day = datetime.today().year
        time_interval = (current_date - date_of_birth).days
        if time_interval < 1:
            data = {
                'status': False,
                'message': 'you are not born yet'
            }
            return Response(data)

        # if current_month > month:
        #     age_year = current_year - year
        #     if current_day >= day:
        #         age_month = current_month - month
        #     else:
        #         age_month = current_month - month - 1
        # elif current_month == month and current_day > day:
        #     age_year = current_year - year
        # else:
        #     age_year = current_year - year - 1
        leap_years = (int(current_year) - int(year))//4
        age_in_years = (int(time_interval) - leap_years)//365
        age_in_months = ((int(time_interval) - leap_years)%365)//30
        age_in_days = ((int(time_interval) - leap_years)%365)%30
        # age = datetime(year=age_in_years, month=age_in_months, day=age_in_days)
        # if time_interval < 1:
        data = {
            'status': True,
            'message': f'your age is {age_in_years} years , {age_in_months} months and {age_in_days} days'
        }
        return Response(data)






