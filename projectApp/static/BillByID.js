$(document).ready(function (){



                  //Get query result on submit
            $('#send_bill_id').on('click', function(e){


                e.preventDefault();
                var bill_id=document.getElementById("bill_id").value;

                $.ajax({
                        type: "GET",
                        url:"http://127.0.0.1:5000//ajax/get_bill_info_by_id",
                        data: {bill_id:bill_id},
                        success:function(response){
                            var bill=response.bill_info;



                            $("#resulttable tbody").html(`<tr>
                                <td id="billID">${bill_id}</td>
                                <td id="buyerName">${bill.buyerName}</td>
                                <td id="makerResult">${bill.maker}</td>
                                <td id="modelResult">${bill.model}</td>
                                <td id="trimResult">${bill.cartrim}</td>
                                <td id="colorResult">${bill.carcolor}</td>
                                <td id="yearResult">${bill.caryear}</td>
                                <td id="conditionResult">${bill.condition}</td>
                                <td id="mileageResult">${bill.mileage}</td>
                                <td id="weightResult">${bill.carweight}</td>
                                <td id="priceResult">${bill.price}</td>
                                </tr>`)

                        },
                        error : function(response){
                            console.log("It's not working")
                            console.log(response)

                         }
            })
            })
        });



