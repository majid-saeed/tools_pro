i m p o r t   n u m p y   a s   n p  
 d e f   r a n d _ n o r m ( N = 1 0 ,   a v g _ = 1 0 ,   s t _ d e v = 1 ,   d e c i = 2 ) :  
         " " "     G e n e r a t e   N   r a n d o m   f l o a t s   w i t h i n   t h e   r a n g e   b e g i n   -   e n d  
         : T e c h n i c a l l y ,   N   r a n d o m   i n t e g e r s   a r e   p r o d u c e d   t h e n   a   r a n d o m  
         : a m o u n t   w i t h i n   0 - 1   i s   a d d e d   t o   t h e   v a l u e  
         " " "  
         f l o a t _ v a l s   =   n p . r a n d o m . n o r m a l ( a v g _ ,   s t _ d e v )     # ,   s i z e = ( N ) )  
         f l o a t _ v a l s   =   n p . a r o u n d ( f l o a t _ v a l s   +   n p . r a n d o m . r a n d ( ) ,   d e c i )     # ( N ) ,   d e c i )  
         r e t u r n   f l o a t _ v a l s  
 _ _ e s r i _ f i e l d _ c a l c u l a t o r _ s p l i t t e r _ _  
 r a n d _ n o r m ( ) 