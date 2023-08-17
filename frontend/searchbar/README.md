# Search Bar Autocompletion | JS, HTML, CSS

- **Title**: "Creating Autocomplete Search Box for Website using HTML, CSS & JavaScript"

1. **Introduction**:
   - Avinash introduces the tutorial on creating an autocomplete search box using HTML, CSS, and JavaScript.
   - Emphasizes the utility of autocomplete search for enhancing user experience.

2. **HTML Structure**:
   - Set up the basic HTML structure with an input field and a button for the search box.
   - Utilize the Font Awesome library for an attractive search icon.
   - Use the `autocomplete="off"` attribute to disable browser autocomplete for the input field.

   ```html
   <div class="search-box">
       <div class="row">
           <input type="text" id="input-box" placeholder="Search anything" autocomplete="off">
           <button><i class="fas fa-search"></i></button>
       </div>
   </div>
   ```

3. **CSS Styling**:
   - Apply CSS to style the search box, input field, and search button.
   - Use Flexbox for alignment and spacing.
   - Set appropriate dimensions, colors, and font properties.

   ```css
   .search-box {
       width: 600px;
       background: white;
       margin: 200px auto 0;
       border-radius: 5px;
   }

   .row {
       display: flex;
       align-items: center;
       padding: 10px 20px;
   }

   #input-box {
       flex: 1;
       height: 50px;
       background: transparent;
       border: 0;
       outline: 0;
       font-size: 18px;
       color: #333;
   }
   /* ... other CSS rules ... */
   ```

4. **JavaScript Interaction**:
   - Implement JavaScript to handle user input and display autocomplete suggestions.
   - Create an array of suggested keywords.
   - Attach an `onkeyup` event to the input field to trigger suggestions.
   - Filter and display relevant suggestions based on user input.

   ```javascript
   const inputBox = document.querySelector('#input-box');
   const resultBox = document.querySelector('.result-box');
   const availableKeywords = ['JavaScript', 'Web Development', 'HTML', /* ... */];

   inputBox.addEventListener('keyup', function () {
       const input = inputBox.value.toLowerCase();
       const filteredKeywords = availableKeywords.filter(keyword =>
           keyword.toLowerCase().includes(input)
       );
       displayResults(filteredKeywords);
   });

   function displayResults(keywords) {
       const content = keywords.map(keyword => `<li>${keyword}</li>`).join('');
       resultBox.innerHTML = `<ul>${content}</ul>`;
   }
   ```

5. **Selecting and Completing**:
   - Allow users to select a suggestion by clicking on it.
   - Populate the input field with the selected suggestion upon click.
   - Hide the suggestion list after selection.

   ```javascript
   resultBox.addEventListener('click', function (event) {
       if (event.target.tagName === 'LI') {
           const selectedKeyword = event.target.textContent;
           inputBox.value = selectedKeyword;
           resultBox.innerHTML = '';
       }
   });
   ```

6. **Conclusion**:
   - The autocomplete search box is now functional, providing real-time suggestions as users type.
   - Avinash encourages viewers to experiment further and apply the concept to their websites.

This summarized guide covers the key aspects and provides code examples for creating an autocomplete search box using HTML, CSS, and JavaScript, catering to beginners.