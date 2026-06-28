class PathFinder:
    def __init__(self, map_data, a, additionals, b):
        print("Initialized")
        self.map = map_data
        self.a = a
        self.b = b
        self.additionals = additionals if additionals else []
        self.objectives = self.additionals + [b]

        self.lines = len(self.map)
        self.cols = len(self.map[0]) if self.lines > 0 else 0

        self.Propag()

    def Propag(self):
        import copy
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
        new_map = copy.deepcopy(self.map)
    
        for r in range(self.lines):
            for c in range(self.cols):
                val = self.map[r][c]
            
                if val in ["1", "2", "3", "4"]:
                    danger_level = int(val)
                
                    for d in directions:
                        nr, nc = r + d[0], c + d[1]
                    
                        if 0 <= nr < self.lines and 0 <= nc < self.cols:
                            neighbor_val = self.map[nr][nc]
                        
                            if neighbor_val != "-0":
                                current_num = int(neighbor_val)
                                new_num = current_num + danger_level
                            
                                if new_num > 5:
                                    new_map[nr][nc] = "5"
                                else:
                                    new_map[nr][nc] = str(new_num)
                                
        self.map = new_map

    def Find(self, pR, pS):
        goods = []
        for r in range(self.lines):
            for c in range(self.cols):
                if self.map[r][c] != "-0":
                    goods.append([r, c])
        
        def Path(start_pos, target_pos):
            attempts = {}
            solutions = []
            finded = False
            
            best_scores_for_case = {tuple(start_pos): 0}
            
            attempts["attempt0"] = {
                "path": [start_pos], 
                "pos": start_pos, 
                "score": 0
            }

            for i in range(2000):
                current_attempt = f"attempt{i}"
                if current_attempt not in attempts:
                    break
            
                pos = attempts[current_attempt]["pos"]
                path = attempts[current_attempt]["path"]
                score = attempts[current_attempt]["score"]

                if pos == target_pos:
                    finded = True
                    solutions.append([path, score])
                    continue

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
                for d in directions:
                    next_pos = [pos[0] + d[0], pos[1] + d[1]]
                    next_pos_tuple = tuple(next_pos)
                
                    if next_pos in goods:
                        danger_cost = int(self.map[next_pos[0]][next_pos[1]]) * pS
                        step_cost = 1 * pR
                        next_score = score - (danger_cost + step_cost)

                        if next_pos_tuple not in best_scores_for_case or next_score > best_scores_for_case[next_pos_tuple]:
                            best_scores_for_case[next_pos_tuple] = next_score
                            
                            next_attempt_id = f"attempt{len(attempts)}"
                            attempts[next_attempt_id] = {
                                "path": path + [next_pos],
                                "pos": next_pos,
                                "score": next_score
                            }
            
            if finded:
                best = max(solutions, key=lambda x: x[1])
                return best[0], best[1]
            return None, None
        global_path = []
        total_score = 0
        current_start = self.a

        for obj in self.objectives:
            sub_path, sub_score = Path(current_start, obj)
            if sub_path is None:
                print(f"Impossible de trouver un chemin jusqu'à l'objectif {obj}")
                return None
            
            if not global_path:
                global_path += sub_path
            else:
                global_path += sub_path[1:]
                
            total_score += sub_score
            current_start = obj

        return global_path, total_score