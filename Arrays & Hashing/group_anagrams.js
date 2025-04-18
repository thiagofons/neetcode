class Solution {
  /**
   * @param {string[]} strs
   * @return {string[][]}
   */
  groupAnagrams(strs) {
    // Total of strings
    let total = strs.length;

    const anagrams = {};

    // Iterate over each string
    for (let i = 0; i < total; i++) {
      const array = new Array(26).fill(0);

      // Count how many characters have in each word
      for (let character of strs[i]) {
        const characterPosition = character.charCodeAt(0) - "a".charCodeAt(0);

        array[characterPosition]++;
      }

      // Use the array as a key of the hashmap
      if (!anagrams[array]) {
        anagrams[array] = 1;
      } else {
        anagrams[array] += 1;
      }

      console.log(anagrams);
    }
  }
}

const strs = ["act", "pots", "tops", "cat", "stop", "hat"];
const solution = new Solution();

console.log(solution.groupAnagrams(strs));
