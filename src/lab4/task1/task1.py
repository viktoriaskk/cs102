from typing import List, Dict, Set


class MovieRecommendationSystem:
    def __init__(self, movies_path: str, history_path: str):
        self.history =[['2', '1', '3'], ['1', '4', '3'], ['2', '2', '2', '2', '2', '3'], ['9', '6', '7'], ['8', '5', '6', '7'], ['2', '9', '5', '6', '8'], ['2', '3', '4', '7', '5', '9']]
        self.movies = {'1': 'Мстители: Финал', '2': 'Хатико', '3': 'Дюна', '4': 'Унесенные призраками', '5': 'Ходячий замок', '6': '1+1', '7': 'Список Шиндлера', '8': 'Крёстный отец', '9': 'Зелёная миля'}

    def read_history(self, path: str) -> List:
        """ This function return all history of other users from file """
        with open(path, 'r', encoding='UTF-8') as history_file:
            return [user.split(',') for user in history_file.read().splitlines()]

    def read_movies(self, path: str) -> Dict:
        """ This function return all movies """
        with open(path, 'r', encoding='UTF-8') as movies_file:
            result = [movie.split(',') for movie in movies_file.read().splitlines()]
            result = {movie[0]:movie[1] for movie in result}
        return result

    def get_views(self, movies: Set) -> Dict[str,int]:
        """ This function returns the number of views for each movie """
        views = {}
        for movie in movies:
            views[movie] = sum(user.count(movie) for user in self.history)
        return views

    def get_recommendations(self, user_history: List) -> str:
        """ This function returns the most viewed recommendation based on user history """
        recommendations = self.get_recommendation_set(user_history)
        recommendations_views = self.get_views(recommendations)

        if len(recommendations) > 0:
            # get the most viewed recommendation
            recommendation_id = max(recommendations_views, key=recommendations_views.get)
            recommendation_name = self.movies[recommendation_id]
            return recommendation_name
        else:
            return 'No any recommendations'

    def get_recommendation_set(self, user_history: List) -> Set:
        """ This function returns all recommendations based on user history """
        result = set()
        for user in self.history:
            coincidence = sum( int(movie in user_history) for movie in user )
            if coincidence > len(user)//2:
                result |= { movie for movie in user if movie not in user_history }
        return result


if __name__ == "__main__":
    movie_file_path = "data/movies.txt"
    history_file_path = "data/history.txt"
    user_views = input("Enter the list of views: ").split(',')
    recommendation_system = MovieRecommendationSystem(movie_file_path, history_file_path)
    recommendation = recommendation_system.get_recommendations(user_views)
    print(recommendation)
