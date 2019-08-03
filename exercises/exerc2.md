
# Exercises, set 2

 1. Create a cli application that counts each word and prints the to 10 most common words in a large file (sorted).

```
a : 131
something : 123
...
```

 2. Create a flask based status reporter. Create something that checks the system load, free memory and disk usage.
 Output the content as a json status message with Flask.

```json
{
  "hostname":"host.name.se",
  "status":"green",
  "message":"ok"
}
```

```json
{
  "hostname":"host.name.se",
  "status":"red",
  "message":"memory full"
}
```

```json
{
  "hostname":"host.name.se",
  "status":"yellow",
  "message":"cpu load high"
}
```
