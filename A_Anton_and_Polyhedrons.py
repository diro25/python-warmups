faces_map={
  "tetrahedron":4,
  "cube":6,
  "octahedron":8,
  "dodecahedron":12,
  "icosahedron":20
}
n=int(input())
total_faces=0
for _ in range(n):
  shape=input()
  total_faces+=faces_map[shape]
print(total_faces)