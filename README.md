# Bookworm

This is a project aimed at mimicing the functionality of GoodReads.com

## Using `ts_generator`

This is a fork from: https://remastr.com/blog/typescript-types-from-drf-serializers

### Todo

- [x] Create a `api-base` class that allows the frontend dev to easily use new endpoints
- [ ] Allow the overriding of `Serializer` names
- [ ] Sorting?
- [ ] Differentiate between an `interface` and a `type`

### Exporting Serializers to React

Run the following to generate and move the TypeScript file to the right place:

```shell
python manage.py generate_types bookworm_core > BaseApi.ts && mv BaseApi.ts ../frontend/common/BaseApi.ts
```