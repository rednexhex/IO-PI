
  table.insert(ctrls, {
    Name = "address",
    ControlType = "Text",
    DefaultValue = 'Enter and IP Address' 
  })
  table.insert(ctrls, {
    Name = "port",
    ControlType = "Knob",
    ControlUnit = "Integer",
    Min = 1,
    Max = 65535,
    DefaultValue = 1081
  })

  table.insert(ctrls, {
    Name = "rly1",
    ControlType = "Button",
    ButtonType = "Trigger",
    UserPin = true,
    PinStyle = "Input",
    Count = 1
  })
  table.insert(ctrls, {
    Name = "rlytime1",
    ControlType = "Knob",
    ControlUnit = "Integer",
    Min = 0,
    Max = 60,
    DefaultValue = 0
  })
  table.insert(ctrls, {
    Name = "rlyled1",
    ControlType = "Indicator",
    IndicatorType = "LED",
    UserPin = false,
    Count = 1
  })

  table.insert(ctrls, {
    Name = "rly2",
    ControlType = "Button",
    ButtonType = "Trigger",
    UserPin = true,
    PinStyle = "Input",
    Count = 1
  })
  table.insert(ctrls, {
    Name = "rlytime2",
    ControlType = "Knob",
    ControlUnit = "Integer",
    Min = 0,
    Max = 60,
    DefaultValue = 0
  })
  table.insert(ctrls, {
    Name = "rlyled2",
    ControlType = "Indicator",
    IndicatorType = "LED",
    UserPin = false,
    Count = 1
  })

  table.insert(ctrls, {
    Name = "rly3",
    ControlType = "Button",
    ButtonType = "Trigger",
    UserPin = true,
    PinStyle = "Input",
    Count = 1
  })
  table.insert(ctrls, {
    Name = "rlytime3",
    ControlType = "Knob",
    ControlUnit = "Integer",
    Min = 0,
    Max = 60,
    DefaultValue = 0
  })
  table.insert(ctrls, {
    Name = "rlyled3",
    ControlType = "Indicator",
    IndicatorType = "LED",
    UserPin = false,
    Count = 1
  })

  table.insert(ctrls, {
    Name = "rly4",
    ControlType = "Button",
    ButtonType = "Trigger",
    UserPin = true,
    PinStyle = "Input",
    Count = 1
  })
  table.insert(ctrls, {
    Name = "rlytime4",
    ControlType = "Knob",
    ControlUnit = "Integer",
    Min = 0,
    Max = 60,
    DefaultValue = 0
  })
  table.insert(ctrls, {
    Name = "rlyled4",
    ControlType = "Indicator",
    IndicatorType = "LED",
    UserPin = false,
    Count = 1
  })
