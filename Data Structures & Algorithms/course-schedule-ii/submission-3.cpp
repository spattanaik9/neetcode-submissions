class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj;
        for (const auto& pair : prerequisites){
            adj[pair[0]].push_back(pair[1]);
        }

        vector<int> res;
        unordered_set<int> visited;
        unordered_set<int> visiting;

        for(int c=0; c<numCourses; c++){
            if (!dfs(adj, c, visited, visiting, res)){
                return {};
            }
        }
        return res;
    }

private:
    bool dfs(const unordered_map<int, vector<int>>& adj, int c, unordered_set<int>& visited, unordered_set<int>& visiting, vector<int>& res){
        if(visiting.count(c)){
            return false;
        }

        if (visited.count(c)){
            return true;
        }

        visiting.insert(c);
        if (adj.count(c)){
            for (int p: adj.at(c)){
                if (!dfs(adj, p, visited, visiting, res)){
                    return false;
                }
            }
        }
        visited.insert(c);
        visiting.erase(c);
        res.push_back(c);
        return true;
    }    
};
