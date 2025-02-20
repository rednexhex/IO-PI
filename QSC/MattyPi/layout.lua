
---  action   ----

layout["address"] = {
  PrettyName = "IP Address",
  Style = "Text",
  TextBoxStyle = "Normal",
  Position = {100, 10},
  Size = {100, 16}
}
layout["port"] = {
  PrettyName = "Port",
  Style = "Text",
  TextBoxStyle = "Normal",
  Position = {100, 30},
  Size = {100, 16}
}
table.insert(graphics, {
  Type = "Text",
  Text = "IP Address:",
  Position = {5, 5},
  Size = {80, 16},
  FontSize = 14,
  HTextAlign = "Right"
})
table.insert(graphics, {
  Type = "Text",
  Text = "Port:",
  Position = {5, 25},
  Size = {80, 16},
  FontSize = 14,
  HTextAlign = "Right"
})



layout["rly1"] = {
    PrettyName = "Relay 1",
    Style = "Button",
    Legend = "Push",
    Position = {30,60},
    Size = {50,16},
    Color = {0,0,0}
  }  
  layout["rlyled1"] = {
    PrettyName = "Relay 1 LED",
    Style = "LED",
    Position = {80,60},
    Size = {15,15},
    Color = {255,0,0}
  }
  layout["rlytime1"] = {
    PrettyName = "Timer 1",
    Style = "Text",
    TextBoxStyle = "Normal",
    Position = {100, 60},
    Size = {20, 16}
  }
  table.insert(graphics, {
    Type = "Text",
    Text = "Relay 1 Pulse Time",
    Position = {125, 60},
    Size = {110, 16},
    FontSize = 12,
    HTextAlign = "Right"
  })
  

  layout["rly2"] = {
    PrettyName = "Relay 2",
    Style = "Button",
    Legend = "Push",
    Position = {30,80},
    Size = {50,16},
    Color = {0,0,0}
  }
  layout["rlyled2"] = {
    PrettyName = "Relay 2 LED",
    Style = "LED",
    Position = {80,80},
    Size = {15,15},
    Color = {255,0,0}
  }
  layout["rlytime2"] = {
    PrettyName = "Timer 2",
    Style = "Text",
    TextBoxStyle = "Normal",
    Position = {100, 80},
    Size = {20, 16}
  }
  table.insert(graphics, {
    Type = "Text",
    Text = "Relay 2 Pulse Time",
    Position = {125, 80},
    Size = {110, 16},
    FontSize = 12,
    HTextAlign = "Right"
  })
  
  
  layout["rly3"] = {
    PrettyName = "Relay 3",
    Style = "Button",
    Legend = "Push",
    Position = {30,100},
    Size = {50,16},
    Color = {0,0,0}
  }
  layout["rlyled3"] = {
    PrettyName = "Relay 3 LED",
    Style = "LED",
    Position = {80,100},
    Size = {15,15},
    Color = {255,0,0}
  }
  layout["rlytime3"] = {
    PrettyName = "Timer 3",
    Style = "Text",
    TextBoxStyle = "Normal",
    Position = {100, 100},
    Size = {20, 16}
  }
  table.insert(graphics, {
    Type = "Text",
    Text = "Relay 3 Pulse Time",
    Position = {125, 100},
    Size = {110, 16},
    FontSize = 12,
    HTextAlign = "Right"
  })

  layout["rly4"] = {
    PrettyName = "Relay 4",
    Style = "Button",
    Legend = "Push",
    Position = {30,120},
    Size = {50,16},
    Color = {0,0,0}
  }
  layout["rlyled4"] = {
    PrettyName = "Relay 4 LED",
    Style = "LED",
    Position = {80,120},
    Size = {15,15},
    Color = {255,0,0}
  }
  layout["rlytime4"] = {
    PrettyName = "Timer 4",
    Style = "Text",
    TextBoxStyle = "Normal",
    Position = {100, 120},
    Size = {20, 16}
  }
  table.insert(graphics, {
    Type = "Text",
    Text = "Relay 4 Pulse Time",
    Position = {125, 120},
    Size = {110, 16},
    FontSize = 12,
    HTextAlign = "Right"
  })
  

table.insert(graphics,{
  Type = "Text",
  Text = "Build Info",
  FontSize = 12,
  HTextAlign = "Left",
  Position = {0, 180},
  Size = {62, 20}
})
table.insert(graphics,{
  Type = "Text",
  Text = "v" .. PluginInfo.BuildVersion,
  FontSize = 12,
  HTextAlign = "Left",
  Position = {0, 200},
  Size = {62, 20}
})

table.insert(graphics,{
  Type="Image",
  Image=logo,
  Position={85,200},
  Size={80,60}
})

table.insert(graphics,{
  Type="Image",
  Image=Signature,
  Position={0,160},
  ZOrder = 1,
  Size={20,23}
})
