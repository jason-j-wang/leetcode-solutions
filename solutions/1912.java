//https://leetcode.com/problems/design-movie-rental-system/description/?envType=daily-question&envId=2025-09-24
class MovieRentingSystem {

    private Map<Integer, Map<Integer, Integer>> stores; 
    private TreeSet<Integer[]> rented; 
    private Map<Integer, TreeSet<Integer[]>> unrented;

    public MovieRentingSystem(int n, int[][] entries) {
        rented = new TreeSet<>((a, b) -> {
            int cmp = a[0].compareTo(b[0]);
            if (cmp != 0) {
                return cmp;
            }
            cmp = a[1].compareTo(b[1]);
            if (cmp != 0) {
                return cmp;
            }

            return a[2].compareTo(b[2]);
        });
        stores = new HashMap<>();
        unrented = new HashMap<>();

        for (int[] entry : entries) {
            int store = entry[0], movie = entry[1], price = entry[2];

            if (!stores.containsKey(store)) {
                stores.put(store, new HashMap<>());
            }

            stores.get(store).put(movie, price);


            if (!unrented.containsKey(movie)) {
                unrented.put(movie, new TreeSet<>((a, b) -> {
                    int cmp = a[0].compareTo(b[0]);
                    if (cmp != 0) {
                        return cmp;
                    }
                    return a[1].compareTo(b[1]);
                }));
            }

            unrented.get(movie).add(new Integer[]{price, store});
        }
        
    }
    
    public List<Integer> search(int movie) {
        List<Integer> ans = new ArrayList<>();
        if (!unrented.containsKey(movie)) {
            return ans;
        }

        Iterator<Integer[]> it = unrented.get(movie).iterator();
        int count = 0;
        

        while (it.hasNext() && count < 5) {
            Integer[] pair = it.next();
            ans.add(pair[1]);
            count++;
        }

        return ans;

    }
    
    public void rent(int shop, int movie) {
        int price = stores.get(shop).get(movie);
        rented.add(new Integer[]{price, shop, movie});
        unrented.get(movie).remove(new Integer[]{price, shop});
    }
    
    public void drop(int shop, int movie) {
        int price = stores.get(shop).get(movie);
        rented.remove(new Integer[]{price, shop, movie});

        unrented.get(movie).add(new Integer[]{price, shop});
    }
    
    public List<List<Integer>> report() {
        Iterator<Integer[]> it = rented.iterator();
        int count = 0;
        List<List<Integer>> ans = new ArrayList<>();

        while (it.hasNext() && count < 5) {
            Integer[] pair = it.next();
            ans.add(new ArrayList<Integer>(Arrays.asList(pair[1], pair[2])));
            count++;
        }

        return ans;
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * List<Integer> param_1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<Integer>> param_4 = obj.report();
 */