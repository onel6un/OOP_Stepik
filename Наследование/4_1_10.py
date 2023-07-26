class Layer:
    def __init__(self) -> None:
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, next_layer):
        self.next_layer = next_layer
        return next_layer


class Input(Layer):
    def __init__(self, inputs) -> None:
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation) -> None:
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        self.ret = self.obj
        return self

    def __next__(self):
        if self.ret:
            layer = self.ret
            self.ret = self.ret.next_layer
            return layer
        else:
            raise StopIteration


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)