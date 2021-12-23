from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp.utils.week_counter import get_week_number


class WeekCounterView(APIView):
    def get(self, request):
        """

        Args:
            request: The request that is being processed

        Returns:
            Response: dict (json) in format {"week": (int)} if success, else {"error": "(str)"}

        """
        if date := request.query_params.get('date'):
            day, month, year = map(int, date.split('_'))
            try:
                weeks_amount = get_week_number(day, month, year)
            except ValueError:
                # catching incorrect date format
                return Response({'error': 'incorrect date'}, status=400, exception=True)
            else:
                # successful response
                return Response({'week': weeks_amount})
        else:
            # catching empty or invalid query params
            return Response({'error': 'empty or not allowed query params'}, status=400, exception=True)
