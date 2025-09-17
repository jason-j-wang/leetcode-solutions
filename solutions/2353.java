//https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2025-09-17
class FoodRatings {

    private Map<String, Integer> foodRating;
    private Map<String, String> foodCuisine;
    private Map<String, PriorityQueue<Pair<Integer, String>>> bestRated;

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        foodRating = new HashMap<>();
        foodCuisine = new HashMap<>();
        bestRated = new HashMap<>();

        for (int i = 0; i < foods.length; i++) {
            foodRating.put(foods[i], ratings[i]);
            foodCuisine.put(foods[i], cuisines[i]);

            if (!bestRated.containsKey(cuisines[i])) {
                bestRated.put(cuisines[i], new PriorityQueue<Pair<Integer, String>>((a, b) -> {
                    int cmp = b.getKey().compareTo(a.getKey());
                    if (cmp == 0) {
                        return a.getValue().compareTo(b.getValue());
                    }

                    return cmp; 
                }));
            }
            bestRated.get(cuisines[i]).add(new Pair<>(ratings[i], foods[i]));
        }
    }
    
    public void changeRating(String food, int newRating) {
        foodRating.put(food, newRating);
        String cuisine = foodCuisine.get(food);

        bestRated.get(cuisine).add(new Pair<>(newRating, food));
    }
    
    public String highestRated(String cuisine) {
        int rating = bestRated.get(cuisine).peek().getKey();
        String food = bestRated.get(cuisine).peek().getValue();
        System.out.println(food);

        while (foodRating.get(food) != rating) {
            bestRated.get(cuisine).poll();
            rating = bestRated.get(cuisine).peek().getKey();
            food = bestRated.get(cuisine).peek().getValue();
        }

        return food;

    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */