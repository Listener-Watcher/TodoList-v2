var Content = React.createClass({
  render.function(){
  var testStyle={fontSize:'18px',marginRight:'20px'};
  return(
    <div className='testClass' style={testStyle}>
    <div>test</div>
      is this text is 18px?
    </div>
  )
  }
});

React.render(
  <Content />,
  document.getElementById('content')
)
