

  address = Controls.address
  port = Controls.port
  rly1 = Controls.rly1
  rly2 = Controls.rly2
  rly3 = Controls.rly3
  rly4 = Controls.rly4
  rlyled1 = Controls.rlyled1
  rlyled2 = Controls.rlyled2
  rlyled3 = Controls.rlyled3
  rlyled4 = Controls.rlyled4
  rlytime1 = Controls.rlytime1
  rlytime2 = Controls.rlytime2
  rlytime3 = Controls.rlytime3
  rlytime4 = Controls.rlytime4


  ----  Sockets   ---
  sock = TcpSocket.New()
  sock.ReadTimeout = 0
  sock.WriteTimeout = 0
  sock.ReconnectTimeout = 5

  -- Constants
  EOL = "\r\n"                       -- End of line character as defined in device's API
  EOLCharacter = TcpSocket.EOL.Lf  -- EOL Character lookup for TCPSocket ReadLine
  

  
  sock.EventHandler = function(sock, evt, err)
    if evt == TcpSocket.Events.Connected then
      print( "socket connected" )
    elseif evt == TcpSocket.Events.Reconnect then
      print( "socket reconnecting..." )
    elseif evt == TcpSocket.Events.Data then
      print( "socket has data" )
      message = sock:ReadLine(TcpSocket.EOL.Any)
      print('rx=',message)
      while (message ~= nil) do
        print( "reading until CrLf got "..message )
        message = sock:ReadLine(TcpSocket.EOL.Any)
      end
    elseif evt == TcpSocket.Events.Closed then
      print( "socket closed by remote" )
    elseif evt == TcpSocket.Events.Error then
      print( "socket closed due to error", err )
    elseif evt == TcpSocket.Events.Timeout then
      print( "socket closed due to timeout" )
    else
      print( "unknown socket event", evt ) --should never happen
    end
  end

  rlytime1 = rlytime1.String
  rlytime2 = rlytime2.String
  rlytime3 = rlytime3.String
  rlytime4 = rlytime4.String

    
Controls.rly1.EventHandler = function()
  sock:Write("relstate,1:1")
  rlyled1.Boolean = true
  TimeInSeconds = rlytime1
  Timer.CallAfter(function()
  sock:Write("setstate,1:1")
  rlyled1.Boolean = false
  end, TimeInSeconds)
end

Controls.rly2.EventHandler = function()
  sock:Write("relstate,2:1")
  rlyled2.Boolean = true
  TimeInSeconds = rlytime2
  Timer.CallAfter(function()
  sock:Write("relstate,2:0")
  rlyled2.Boolean = false
  end, TimeInSeconds)
end     

Controls.rly3.EventHandler = function()
  sock:Write("relstate,3:1")
  rlyled3.Boolean = true
  TimeInSeconds = rlytime3
  Timer.CallAfter(function()
  sock:Write("relstate,3:0")
  rlyled3.Boolean = false
  end, TimeInSeconds)
end

Controls.rly4.EventHandler = function()
  sock:Write("relstate,4:1")
  rlyled4.Boolean = true
  TimeInSeconds = rlytime4
  Timer.CallAfter(function()
  sock:Write("relstate,4:0")
  rlyled4.Boolean = false
  end, TimeInSeconds)
end

sock:Connect(address.String, port.Value)