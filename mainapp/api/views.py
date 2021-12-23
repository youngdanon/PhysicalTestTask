from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils.week_counter import get_week_number


class WeekCounterView(APIView):
    def get(self, request):
        if request.query_params.get('date'):
            day, month, year = map(int, request.query_params.get('date').split('_'))
            try:
                weeks_amount = get_week_number(day, month, year)
            except ValueError:
                return Response({'error': 'incorrect date'}, status=400, exception=True)
            else:
                return Response({'week': weeks_amount})
        else:
            return Response({'error': 'empty request query'}, status=400, exception=True)
