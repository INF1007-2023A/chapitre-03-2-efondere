#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	return voltage**2 / resistance

def orthogonal(v1, v2):
	# NOTE: orthogonal means perpendicular...
	return v1[0] * v2[0] + v1[1] * v2[1] == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	total = count = 0

	for v in values:
		if v < 0:
			continue
		total += v
		count += 1

	return total / count

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0

	while value != 0:
		if value >= 20:
			twenties += 1
			value -= 20
		elif value >= 10:
			tens += 1
			value -= 10
		elif value >= 5:
			fives += 1
			value -= 5
		elif value >= 1:
			ones += 1
			value -= 1

	return (twenties, tens, fives, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)

	while abs_value != 0:
		result = digit_letters[abs_value % base] + result
		abs_value //= base

	if value < 0:
		result = "-" + result

	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
