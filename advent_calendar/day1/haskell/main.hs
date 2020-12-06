import Data.List

main :: IO ()
main = do
  input <- readFile "input"
  let lns = map read $ lines input
  let entries = nub [x | x <- lns, y <- lns, z <- lns, x + y + z == 2020]
  print $ entries
  print $ product entries