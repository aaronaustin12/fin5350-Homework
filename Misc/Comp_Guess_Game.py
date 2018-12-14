{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The computer guesses... 50\n",
      "The computer guesses... 75\n",
      "The computer guesses... 88\n",
      "The computer guesses... 94\n",
      "The computer guesses... 97\n",
      "The computer guesses... 99\n",
      "And the computer guessed 99 and thats the right answer!\n"
     ]
    }
   ],
   "source": [
    "def computer_guess(num):\n",
    "    low = 1\n",
    "    high = 100\n",
    "    guess = 50\n",
    "    while guess != num:\n",
    "        guess = (low+high)//2\n",
    "        print(\"The computer guesses...\", guess)\n",
    "        if guess > num:\n",
    "            high = guess\n",
    "        elif guess < num:\n",
    "            low = guess +1\n",
    "            \n",
    "    print(\"And the computer guessed\", guess, \"and thats the right answer!\")\n",
    "\n",
    "    \n",
    "def main():\n",
    "    num = int(input(\"Enter a number:\"))\n",
    "    if num < 1 or num > 100:\n",
    "        print(\"Must be in range[1,100]\")\n",
    "    else:\n",
    "        computer_guess(num)\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    main()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
