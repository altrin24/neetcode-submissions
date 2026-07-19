
class Solution {


    public boolean isAnagram(String s, String t) {
       Map<Character, Integer> map = new HashMap<>();

for (char ch : s.toCharArray()) {
    map.merge(ch, 1, Integer::sum);
}
        Map<Character, Integer> map1 = new HashMap<>();

for (char ch : t.toCharArray()) {
    map1.merge(ch, 1, Integer::sum);
}

    

       return map.equals(map1);

    }
}
