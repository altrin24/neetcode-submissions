class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        
        Map<Integer, Long> result = Arrays.stream(nums).boxed()
        .collect(Collectors.groupingBy(
                num->num,
                Collectors.counting()))
        .entrySet()
        .stream()
        .sorted(Map.Entry.<Integer, Long>comparingByValue().reversed())
        .collect(Collectors.toMap(
                Map.Entry::getKey,
                Map.Entry::getValue,
                (a, b) -> a,
                LinkedHashMap::new
        ));

       return result.keySet()
        .stream()
        .limit(k)
        .mapToInt(Integer::intValue)
        .toArray();
        

        
    }
}
