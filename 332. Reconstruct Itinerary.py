from typing import List

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
class Solution:
    result = []
    end_state = False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        ticket_graph = {}
        Solution.result = []
        Solution.end_state = False
        for i in tickets:
            if i[0] not in ticket_graph:
                ticket_graph[i[0]] = [i[1]]
            else:
                ticket_graph[i[0]].append(i[1])

        for i in ticket_graph:
            ticket_graph[i].sort(reverse=True)


        print(ticket_graph)


        def findCity(path:[],city:str,ticket_graph_map:{},visited:{},answer:int):
            path.append(city)

            if answer==len(visited):
                Solution.end_state = True
                Solution.result = path

            if city in ticket_graph_map and len(ticket_graph_map[city])>0:
               #print(path,city,visited)
               for i in range(len(ticket_graph_map[city])):
                   current_index = len(ticket_graph_map[city]) - 1 - i
                   if city+str(current_index) in visited:
                       continue
                   if Solution.end_state:
                       break

                   next_city=  ticket_graph_map[city][current_index]
                   new_visited = visited.copy()
                   new_visited[city+str(current_index)] =1
                   findCity(path[:],next_city,ticket_graph_map,new_visited,answer)

        findCity([],"JFK",ticket_graph,{},len(tickets))

        return Solution.result


print(Solution.findItinerary(Solution,tickets))