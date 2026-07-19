class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
         Map<String, List<String>> groupAnagrams = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);

            String key = new String(chars);

            List<String> list = groupAnagrams.getOrDefault(key, new ArrayList<>());
            list.add(str);

            groupAnagrams.put(key, list);
        }

        return new ArrayList<>(groupAnagrams.values());
    }
}
