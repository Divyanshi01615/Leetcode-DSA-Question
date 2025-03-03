class Solution {
public:
    void dfs(vector<vector<int>>& rooms, int v, vector<bool>& visited) {
        visited[v] = true;
        for (auto &i : rooms[v]) {
            if (!visited[i]) {
                dfs(rooms, i, visited);
            }
        }
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        dfs(rooms, 0, visited);
        for (int i = 0; i < n; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }
};