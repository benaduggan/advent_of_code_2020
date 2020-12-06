main = do
  input <- readFile "input"
  let lns = (map read $ lines input) :: [Int]
