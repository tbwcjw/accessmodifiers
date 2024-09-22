# accessmodifiers

Access control system using Python decorators and metaclasses to enforce visibility levels on classes and methods.

## Features

- Define methods with different access levels using decorators.
- Uses a metaclass to enforce access rules at runtime.

## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/access-control-system.git
cd access-control-system
```

### Usage

   ```python
   from access import public_class, protected_class, private_class, public, protected, private

   @public_class
   class ExampleClass:
       @public
       def public_method(self):
           return "This is a public method."

       @protected
       def protected_method(self):
           return "This is a protected method."

       @private
       def private_method(self):
           return "This is a private method."
```

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
