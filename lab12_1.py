"""asd"""
import json
def main(amt, m_n):
    """asdas"""
    ans = ["10 baht = 0 coins", "5 baht = 0 coins", "2 baht = 0 coins", "1 baht = 0 coins"]
    c_t = 0
    print("Amount:", amt)
    while True:
        if amt <= 0:
            print("Coin exchange result:")
            for result in ans:
                print(" ", result)
            print("Number of coins:", c_t)
            break
        if amt > 0 and m_n["10"] <= 0 and m_n["5"] <= 0 and m_n["2"] <= 0 and m_n["1"] <= 0:
            print("Coins are not enough.")
            break

        for i, coin_value in enumerate([10, 5, 2, 1]):
            if amt >= coin_value and m_n[str(coin_value)] > 0:
                num_coins = min(amt // coin_value, m_n[str(coin_value)])
                ans[i] = str(coin_value) +" baht = " + str(num_coins) + " coins"
                c_t += num_coins
                amt -= num_coins * coin_value
                m_n[str(coin_value)] -= num_coins
                break

main(int(input()), json.loads(input()))