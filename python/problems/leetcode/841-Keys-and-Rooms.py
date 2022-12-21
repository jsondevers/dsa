from typing import List

# Time: O(N + K) where n is number of rooms and e is number of keys
# Space: O(N) bc we create a stack that can have at most N rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_keys = [0]
        seen = set()

        while room_keys:
            room = room_keys.pop()
            if room in seen:
                continue
            seen.add(room)
            room_keys.extend(rooms[room])

        return len(seen) == len(rooms)
