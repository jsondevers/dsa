/*
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is
higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible
results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
*/

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 */
int guess(int num);

/*
Time: O(logN)
Space: O(1)
Binary Search
*/
class Solution {
 public:
  int guessNumber(int n) {
    int left = 0, right = n;

    while (left <= right) {
      int mid = left + (right - left) / 2;

      if (guess(mid) == -1) {
        right = mid - 1;
      } else if (guess(mid) == 1) {
        left = mid + 1;
      } else {
        return mid;
      }
    }
    return 0;
  }
};
