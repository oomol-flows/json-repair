<div align=center>
  <h1>JSON Repair</h1>
  <p>
    <a href="https://github.com/oomol-flows/json-repair/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/oomol-flows/json-repair" alt="license" /></a>
  </p>
  <p><a href="https://hub.oomol.com/package/json-repair?open=true" target="_blank"><img src="https://static.oomol.com/assets/button.svg" alt="Open in OOMOL Studio" /></a></p>
</div>

[中文文档](./README_zh.md)

## What is JSON Repair?

JSON Repair is a powerful block that automatically fixes broken or malformed JSON data. Whether you're dealing with incomplete JSON files, missing quotes, trailing commas, or other formatting issues, this block intelligently repairs them to create valid JSON output.

## Why Use JSON Repair?

- **Fix Common Issues**: Automatically handles missing quotes, brackets, commas, and other JSON syntax errors
- **Save Time**: No need to manually search and fix JSON formatting problems
- **Reliable**: Built on the proven `json_repair` library
- **User-Friendly**: Simple interface with customizable formatting options
- **Preview Support**: See the repaired JSON before using it in your workflow

## How to Use

### JSON Repair Block

![](./static/1.png)

The JSON Repair block takes broken JSON and outputs clean, properly formatted JSON.

### Input Parameters

| Parameter | Description | Example | Default |
|-----------|-------------|---------|---------|
| **content** | The JSON content that needs to be fixed | `{"name": "John" "age": 30,}` | `{}` |
| **indent** | How many spaces to use for formatting. Set to `0` for single-line output | `2`, `4`, or `0` | `2` |
| **preview** | Show a preview of the repaired JSON | `true` or `false` | `true` |

### Output

- **output**: The repaired and properly formatted JSON content

### Example Usage

**Input (Broken JSON):**
```json
{"name": "John" "age": 30, "city": "New York",}
```

**Output (Repaired JSON):**
```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

## Common Use Cases

1. **API Response Cleaning**: Fix malformed JSON responses from APIs
2. **Data Migration**: Clean up JSON files during data transfer
3. **Configuration Files**: Repair broken config files
4. **Log Processing**: Fix JSON logs with formatting issues
5. **Development**: Quickly fix JSON during testing and development

## Getting Started

1. Add the JSON Repair block to your OOMOL workflow
2. Connect your broken JSON data to the `content` input
3. Adjust the `indent` setting for your preferred formatting
4. Enable `preview` to see the results before processing
5. Use the `output` in the next step of your workflow

## Tips

- **Single Line Output**: Set `indent` to `0` for compact, single-line JSON
- **Pretty Formatting**: Use `indent` values of `2` or `4` for readable, formatted JSON
- **Preview First**: Enable preview to verify the repair before using the output
- **Test with Sample Data**: Try with a small sample of your data first

## Acknowledgments

This project is built upon the excellent [json_repair](https://github.com/mangiucugna/json_repair) Python library. 