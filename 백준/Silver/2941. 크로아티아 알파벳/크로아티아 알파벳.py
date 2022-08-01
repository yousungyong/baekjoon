TE = input()
alpha = len(TE)

if '-' in TE :
  alpha -= TE.count('-')

if 'lj' in TE :
  alpha -= TE.count('lj')

if 'nj' in TE :
  alpha -= TE.count('nj')

if '=' in TE : ## ddz=z=
  alpha -= TE.count('=')
  alpha -= TE.count('dz=')

print(alpha)