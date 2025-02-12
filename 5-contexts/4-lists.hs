processNumbers :: [Int] -> Int
processNumbers numbers = sum [ x^2 | x <- numbers, odd x]

cartesianProduct xs ys = [ (x, y) | x <- xs, y <- ys]

cartesianProduct' xs ys = do
    x <- xs
    y <- ys
    pure (x, y)

cartesianProduct'' xs ys = liftA2 (,) xs ys

cartesianProduct''' xs ys = xs >>= \x -> ys >>= pure . (x,)

test = pairs == pairs' && pairs' == pairs''
        && processNumbers [1..10] == 165
  where
    pairs = cartesianProduct [1,2,3] ['a', 'b']
    pairs' = cartesianProduct' [1,2,3] ['a', 'b']
    pairs'' = cartesianProduct'' [1,2,3] ['a', 'b']
    pairs''' = cartesianProduct''' [1,2,3] ['a', 'b']
